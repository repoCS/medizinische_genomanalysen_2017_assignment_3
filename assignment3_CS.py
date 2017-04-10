#!/usr/bin/env python2

import vcf
from vcf import utils
import hgvs

__author__ = 'Clemens Spielvogel'


class Assignment3:
    def __init__(self):
        # Check if pyvcf is installed
        print "PyVCF version: %s" % vcf.VERSION

        # Check if hgvs is installed
        print "HGVS version: %s" % hgvs.__version__

        # Initialize reader for the three vcf files
        self.vcf_reader_mother = vcf.Reader(open('AmpliseqExome.20141120.NA24143.vcf', 'r'))
        self.vcf_reader_father = vcf.Reader(open('AmpliseqExome.20141120.NA24149.vcf', 'r'))
        self.vcf_reader_son = vcf.Reader(open('AmpliseqExome.20141120.NA24385.vcf', 'r'))


    def get_total_number_of_variants_mother(self):
        '''
        Return the total number of identified variants in the mother
        :return:
        '''
        number_of_variants_mother = 0
        for record in self.vcf_reader_mother:
            number_of_variants_mother += 1

        print "Number of variants (mother):", number_of_variants_mother
        return number_of_variants_mother


    def get_total_number_of_variants_father(self):
        '''
        Return the total number of identified variants in the father
        :return:
        '''
        number_of_variants_father = 0
        for record in self.vcf_reader_father:
            number_of_variants_father += 1

        print "Number of variants (father):", number_of_variants_father
        return number_of_variants_father
    

    def get_variants_shared_by_father_and_son(self):
        '''
        Return the number of identified variants shared by father and son
        :return:
        '''
        records = 0
        for record in self.vcf_reader_father:
            if record in self.vcf_reader_son:
                records += 1

        print records
        return records


    def get_variants_shared_by_mother_and_son(self):
        '''
        Return the number of identified variants shared by mother and son
        :return:
        '''
        records = 0
        for record in self.vcf_reader_mother:
            if record in self.vcf_reader_son:
                records += 1

        print records
        return records


    def get_variants_shared_by_trio(self):
        '''
        Return the number of identified variants shared by father, mother and son
        :return:
        '''
        records = 0
        for record in self.vcf_reader_father:
            if record in self.vcf_reader_son and record in self.vcf_reader_mother:
                records += 1

        print records
        return records


    def merge_mother_father_son_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of the trio (merge VCFs)
        :return:
        '''
        merge_file = open("merge_file.vcf", "w")
        writer = vcf.Writer(merge_file, self.vcf_reader_mother, "\n")

        for records in utils.walk_together(self.vcf_reader_mother, self.vcf_reader_father, self.vcf_reader_son):
            for entry in records:
                if entry is not None:
                    writer.write_record(entry)

        print("Successfully merged files.")


    def convert_first_variants_of_son_into_HGVS(self):
        '''
        Convert the first 100 variants identified in the son into the corresponding transcript HGVS.
        Each variant should be mapped to all corresponding transcripts. Pointer:
        - https://hgvs.readthedocs.io/en/master/examples/manuscript-example.html#project-genomic-variant-to-a-new-transcript
        :return:
        '''
        print("TODO")


    def print_summary(self):
        self.get_total_number_of_variants_mother()
        self.get_total_number_of_variants_father()
        self.get_variants_shared_by_father_and_son()
        self.get_variants_shared_by_mother_and_son()
        self.get_variants_shared_by_trio()
        self.merge_mother_father_son_into_one_vcf()
        self.convert_first_variants_of_son_into_HGVS()



if __name__ == '__main__':
    print("Assignment 3")
    assignment1 = Assignment3()
assignment1.print_summary()
