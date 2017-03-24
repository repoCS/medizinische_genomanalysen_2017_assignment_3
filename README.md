# Medizinische Genomanalysen 2017 - Assignment 3

## Overview
* Fork and clone the repository
* Complete the python program, based on the template, to calculate various properties
* Push to your repository

## Attention!
As the HGVS package does only support Python2, please run the script with Python2

## Data
* Son
  * HG002-NA24385-huAA53E0
  * ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/data/AshkenazimTrio/analysis/IonTorrent_TVC_03162015/AmpliseqExome.20141120.NA24385.vcf
* Mother
  * HG004-NA24143-hu8E87A9
  * ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/data/AshkenazimTrio/analysis/IonTorrent_TVC_03162015/AmpliseqExome.20141120.NA24143.vcf
* Father
  * HG003-NA24149-hu6E4515
  * ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/data/AshkenazimTrio/analysis/IonTorrent_TVC_03162015/AmpliseqExome.20141120.NA24149.vcf
  
## Tools
* pyvcf (http://pyvcf.readthedocs.io/en/latest/)
* hgvs (https://hgvs.readthedocs.io/en/master/) - only works with Python 2

## Hints for HGVS
The following example is for version 1.0.0a1.<br/>
Please see http://hgvs.readthedocs.io/en/master/changelog/1.0/1.0.0a1.html for changes
```python

import hgvs.dataproviders.uta
import hgvs.parser
from bioutils.assemblies import make_name_ac_map

## Connect to UTA
hdp = hgvs.dataproviders.uta.connect()

## Used to get the transcripts
assembly_mapper = hgvs.assemblymapper.AssemblyMapper(hdp) # EasyVariantMapper before

## Used for parsing
hgvsparser = hgvs.parser.Parser() # Parser

## Now for each variant

    ## Get chromosome mapping
    refseq_nc_number = make_name_ac_map("GRCh37.p13")[record.CHROM[3:]]
    ## Format: nc_number :g. position reference > alternative
    genome_hgvs = "%s:g.%s%s>%s" % (refseq_nc_number, str(record.POS), str(record.REF), str(record.ALT[0]))
            
    ## Now parse the variant
    ## http://hgvs.readthedocs.io/en/master/modules/io.html?highlight=parser_hgvs

```
