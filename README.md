# penicillin-pneumo-rf

This repository hosts the docker image file and data files for a prediction container that predicts penicillin resistance from *S. pneumoniae* whole genome sequencing data.
It uses data featured in the [pyseer example](https://pyseer.readthedocs.io/en/master/tutorial.html). It is a proof of principal to show how [tb-ml](https://github.com/jodyphelan/tb-ml) can be extended to run on non-TB data. It takes a couple of shortcuts and shouldn't be used in production (specifically it sets any missing positions to reference, which is not best practice). The model is a random forest that has been trained on genome-wide SNPs (training code in script directory).

It requires a vcf file as input and can be run through `tb-ml` with:

```
tb-ml --container jodyphelan/penicillin-pneumo-rf:latest "--vcf yoursample.vcf.gz"
```

For example you can use the test data in this repository:

```
tb-ml --container jodyphelan/penicillin-pneumo-rf:latest "--vcf /example/test.vcf.gz"
```

This conainer can be chaned to any pre-processing container that writes a vcf file.