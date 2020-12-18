FROM continuumio/miniconda3:4.8.2

SHELL ["/bin/bash", "-c"]
RUN conda init bash
RUN echo "source activate testenv" > ~/.bashrc

RUN conda create \
    --name testenv \
    --override-channels -c conda-forge \
    -y \
    --quiet \
    python=3.8 \
    pandas

COPY ./model.py /model.py
COPY ./run_model /run_model

CMD /run_model
