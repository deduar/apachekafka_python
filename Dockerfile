FROM python:3.9.4

RUN groupadd --gid 1000 coinscrap_group && \
  useradd --uid 1000 --system -m -d /home/coinscrap -g coinscrap_group coinscrap && \
  mkdir -p /app && \
  chown coinscrap:coinscrap_group /app

COPY --chown=1000:1000 . /app

WORKDIR /app
USER 1000
ENV PATH="/home/coinscrap/.local/bin:${PATH}"
RUN pip install --no-cache-dir --user -r requeriments.txt
RUN pip install --no-cache-dir --user libs/carbon_footprint-0.0.1-py3-none-any.whl

CMD [ "python", "-m", "consumer", "aba_cfp_consumer"]