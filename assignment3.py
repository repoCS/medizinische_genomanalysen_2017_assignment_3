#! /usr/bin/env python2

import vcf
import hgvs

__author__ = 'XXX'


class Assignment3:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        ## Check if hgvs is installed
        print("HGVS version: %s" % hgvs.__version__)
        

    def get_total_number_of_variants_mother(self):
        '''
        Return the total number of identified variants in the mother
        :return: 
        '''
        print("TODO")
        
        
    def get_total_number_of_variants_father(self):
        '''
        Return the total number of identified variants in the father
        :return: 
        '''
        print("TODO")
       
        
    def get_variants_shared_by_father_and_son(self):
        '''
        Return the number of identified variants shared by father and son
        :return: 
        '''
        print("TODO")
        
        
    def get_variants_shared_by_mother_and_son(self):
        '''
        Return the number of identified variants shared by mother and son
        :return: 
        '''
        print("TODO")
        
    def get_variants_shared_by_trio(self):
        '''
        Return the number of identified variants shared by father, mother and son
        :return: 
        '''
        print("TODO")
        

    def merge_mother_father_son_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of the trio (merge VCFs)
        :return: 
        '''
        print("TODO")
        
        
    def convert_first_variants_of_son_into_HGVS(self):
        '''
        Convert the first 100 variants identified in the son into the corresponding transcript HGVS.
        Each variant should be mapped to all corresponding transcripts. Pointer:
        - https://hgvs.readthedocs.io/en/master/examples/manuscript-example.html#project-genomic-variant-to-a-new-transcript
        :return: 
        '''
        print("TODO")
        
    
    def print_summary(self):
        print("Print all results here")
    
        
if __name__ == '__main__':
    print("Assignment 3")
    assignment1 = Assignment3()
    assignment1.print_summary()
    
    

