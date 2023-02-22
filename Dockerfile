FROM mambaorg/micromamba:latest

LABEL software.version="0.4.0"
LABEL image.name="jodyphelan/penicillin-pneumo-rf"
ARG MAMBA_DOCKERFILE_ACTIVATE=1
RUN micromamba install -y -n base -c bioconda -c conda-forge \
    python \
    scikit-learn=1.2.1 \
    bcftools=1.16 \
    tqdm && \
    micromamba clean --all --yes

# create a directory for the internal data used by the container
USER root
RUN mkdir /internal_data /data
# copy the model, data files, and scripts
COPY data_files/model.pkl /internal_data/model.pkl
COPY scripts/predict_outcome.py /internal_data

# set `/data` as working directory so that the output is written to the
# mount point when run with `docker run -v $PWD:/data ... -o output.csv`
WORKDIR /data

# ENTRYPOINT ["/opt/conda/bin/python", "/internal_data/predict_outcome.py", "--model", "/internal_data/model.pkl"]
ENTRYPOINT ["/usr/local/bin/_entrypoint.sh", "python", "/internal_data/predict_outcome.py", "--model", "/internal_data/model.pkl"]
