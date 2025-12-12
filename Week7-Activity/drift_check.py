import pandas as pd
from evidently import Report, Dataset, DataDefinition
from evidently.presets import DataDriftPreset

train = pd.read_csv("data/train.csv")
production = pd.read_csv("data/test.csv")


train_data = Dataset.from_pandas(
    train,
    data_definition=DataDefinition()
)

production_data = Dataset.from_pandas(
    production,
    data_definition=DataDefinition()
)


report = Report([
    DataDriftPreset()
])

result = report.run(
    current_data=production_data,
    reference_data=train_data
)
result.save_html("drift_report.html")
