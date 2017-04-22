#!/usr/bin/env python2

'''
Assignment 2 - Medizinische Genomanalyse
von Clemens Spielvogel

Das Skript muss mit Python 2 ausgefuehrt werden!

VOR DEM AUSFUEHREN muss der absolute Pfad der vcf-Dateien fuer die drei Personen, in den vcf Variablen (Zeile 22 - 24)
angegeben werden!
'''

import vcf
from vcf import utils
import hgvs
import hgvs.dataproviders.uta
import hgvs.parser
import hgvs.assemblymapper
from bioutils.assemblies import make_name_ac_map

__author__ = 'Clemens Spielvogel'

vcf_son = "/home/vortex/Bioinformatik/med_genomanalyse/AmpliseqExome.20141120.NA24385.vcf"
vcf_mother = "/home/vortex/Bioinformatik/med_genomanalyse/AmpliseqExome.20141120.NA24143.vcf"
vcf_father = "/home/vortex/Bioinformatik/med_genomanalyse/AmpliseqExome.20141120.NA24149.vcf"

class Assignment3:
    def __init__(self, vcf_son, vcf_mother, vcf_father):
        self.vcf_son = vcf_son
        self.vcf_mother = vcf_mother
        self.vcf_father = vcf_father

        # Check if pyvcf is installed
        print "PyVCF version: %s" % vcf.VERSION

        # Check if hgvs is installed
        print "HGVS version: %s" % hgvs.__version__


    def get_total_number_of_variants_mother(self):
        '''
        Return the total number of identified variants in the mother
        :return:
        '''

        print "\n---------------"

        vcf_readermother = vcf.Reader(open(self.vcf_mother, 'r'))

        number_of_variants_mother = 0
        for record in vcf_readermother:
            number_of_variants_mother += 1

        print "Number of variants (mother):", number_of_variants_mother
        return number_of_variants_mother


    def get_total_number_of_variants_father(self):
        '''
        Return the total number of identified variants in the father
        :return:
        '''

        print "\n---------------"

        vcf_readerfather = vcf.Reader(open(self.vcf_father, 'r'))   # Readerfunktion fuer vcf oeffnen

        number_of_variants_father = 0   # Initialisierung der Variable fuer gemeinsame Varianten
        for record in vcf_readerfather:     # Iteration durch Reader
            number_of_variants_father += 1  # Erhoehung um Eins fuer jede gemeinsame Variante

        print "Number of variants (father):", number_of_variants_father
        return number_of_variants_father
    

    def get_variants_shared_by_father_and_son(self):
        '''
        Return the number of identified variants shared by father and son
        :return:
        '''

        print "\n---------------\nVariants shared by father and son:"

        vcf_readerfather = vcf.Reader(open(self.vcf_father, 'r'))
        vcf_readerson = vcf.Reader(open(self.vcf_son, 'r'))

        records = 0
        for record in vcf.utils.walk_together(vcf_readerfather, vcf_readerson):
            if not record[0] is None and not record[1] is None:
                records += 1

        print records
        return records


    def get_variants_shared_by_mother_and_son(self):
        '''
        Return the number of identified variants shared by mother and son
        :return:
        '''

        print "\n---------------\nVariants shared by mother and son:"

        vcf_readermother = vcf.Reader(open(self.vcf_mother, 'r'))
        vcf_readerson = vcf.Reader(open(self.vcf_son, 'r'))

        records = 0
        records = 0
        for record in vcf.utils.walk_together(vcf_readerson, vcf_readermother):
            if not record[0] is None and not record[1] is None:
                records += 1

        print records
        return records


    def get_variants_shared_by_trio(self):
        '''
        Return the number of identified variants shared by father, mother and son
        :return:
        '''

        print "\n---------------\nVariants shared by father, mother and son:"

        vcf_readerson = vcf.Reader(open(self.vcf_son, 'r'))
        vcf_readermother = vcf.Reader(open(self.vcf_mother, 'r'))
        vcf_readerfather = vcf.Reader(open(self.vcf_father, 'r'))

        records = 0
        for record in vcf.utils.walk_together(vcf_readerson, vcf_readermother, vcf_readerfather):
            if not record[0] is None and not record[1] is None and not record[2] is None:
                records += 1

        print records
        return records


    def merge_mother_father_son_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of the trio (merge VCFs)
        :return:
        '''

        print "\n---------------\nMerging files.."

        vcf_readerson = vcf.Reader(open(self.vcf_son, 'r'))
        vcf_readermother = vcf.Reader(open(self.vcf_mother, 'r'))
        vcf_readerfather = vcf.Reader(open(self.vcf_father, 'r'))

        merge_file = open("merge_file.vcf", "w")
        writer = vcf.Writer(merge_file, vcf_readermother, "\n")

        for records in utils.walk_together(vcf_readermother, vcf_readerfather, vcf_readerson):
            for entry in records:
                if entry is not None:
                    writer.write_record(entry)

        print("Successfully merged files: Outputfile = merge_file.vcf")


    def convert_first_variants_of_son_into_HGVS(self):
        '''
        Convert the first 100 variants identified in the son into the corresponding transcript HGVS.
        Each variant should be mapped to all corresponding transcripts. Pointer:
        - https://hgvs.readthedocs.io/en/master/examples/manuscript-example.html#project-genomic-variant-to-a-new-transcript
        :return:
        '''

        print "\n---------------\nConverting first 100 variants of son to HGVS.."

        vcf_readerson = vcf.Reader(open(self.vcf_son, 'r'))
        output_file = open("hgvs_file", "w")

        proccessed_variants = 0
        succ_proc_variants = 0
        exceptions = 0

        # UTA Verbindung
        uta = hgvs.dataproviders.uta.connect()
        assembly_mapper = hgvs.assemblymapper.AssemblyMapper(uta, normalize=False)

        # Parsing
        hgvs_parser = hgvs.parser.Parser()

        for read in vcf_readerson:
            if proccessed_variants < 100:
                refseq_nc_number = make_name_ac_map("GRCh37.p13")[read.CHROM[3:]]
                genome_hgvs ="{}:g.{}{}>{}".format(refseq_nc_number, str(read.POS), str(read.REF), str(read.ALT[0]))

                try:
                    hgvs_variant = hgvs_parser.parse_hgvs_variant(genome_hgvs)
                    for transcript in assembly_mapper.relevant_transcripts(hgvs_variant):
                        try:
                            coding = assembly_mapper.g_to_c(hgvs_variant, transcript)
                            succ_proc_variants += 1
                            print "{}\t{}".format(hgvs_variant, coding)
                            output_file.write("{}\t{}".format(hgvs_variant, coding))

                        except hgvs.exceptions.HGVSUsageError:
                            noncoding = assembly_mapper.g_to_n(hgvs_variant, transcript)
                            succ_proc_variants += 1
                            print "{}\t{}".format(hgvs_variant, noncoding)
                            output_file.write("{}\t{}".format(hgvs_variant, noncoding))

                        except:
                            exceptions += 1

                except Exception:
                    exceptions += 1

            else:
                break

            proccessed_variants += 1

        output_file.close()

        print "Successful conversions: %s" % (succ_proc_variants)
        print "Exceptions occurred: %s" % (exceptions)


    def print_summary(self):
        self.get_total_number_of_variants_mother()
        self.get_total_number_of_variants_father()
        self.get_variants_shared_by_father_and_son()
        self.get_variants_shared_by_mother_and_son()
        self.get_variants_shared_by_trio()
        self.merge_mother_father_son_into_one_vcf()
        self.convert_first_variants_of_son_into_HGVS()



if __name__ == '__main__':
    print "Assignment 3"
    assignment1 = Assignment3(vcf_son , vcf_mother, vcf_father)
    assignment1.print_summary()
