.PHONY: create_data_lake
.PHONY: ingest_data
.PHONY: transform_data
.PHONY: clean_data
.PHONY: compute_daily_prices
.PHONY: pipeline
.PHONY: make_features
.PHONY: train_model

create_data_lake:
	python3 src/data/create_data_lake.py

ingest_data:
	python3 src/data/ingest_data.py

transform_data:
	python3 src/data/transform_data.py

clean_data:
	python3 src/data/clean_data.py

compute_daily_prices:
	python3 src/data/compute_daily_prices.py

compute_monthly_prices:
	python3 src/data/compute_monthly_prices.py

pipeline:
	rm -rf data_lake
	python3 src/data/create_data_lake.py
	python3 src/data/pipeline.py

make_daily_prices_plot:
	python3 src/visualization/make_daily_prices_plot.py

make_monthly_prices_plot:
	python3 src/visualization/make_monthly_prices_plot.py

make_features:
	python3 src/features/make_features.py

train_model:
	python3 src/models/train_daily_model.py

make_forecasts:
	python3 src/models/make_forecasts.py

