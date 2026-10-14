# APIDirectCertification

Students directly certified for free meals in one school year (API 3.1): approved automatically, without a meal application, through SNAP, TANF, FDPIR or Medicaid (most states), or because they are homeless, migrant, runaway, in foster care or in Head Start. Usually lower than free/reduced lunch eligibility and not comparable to it. Collected from 2016-17.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of students directly certified for free meals | [optional] 
**percent** | **float** | Percent of enrolled students excluding pre-kindergarten (0-100, two decimals) | [optional] 

## Example

```python
from schooldigger.models.api_direct_certification import APIDirectCertification

# TODO update the JSON string below
json = "{}"
# create an instance of APIDirectCertification from a JSON string
api_direct_certification_instance = APIDirectCertification.from_json(json)
# print the JSON string representation of the object
print(APIDirectCertification.to_json())

# convert the object into a dict
api_direct_certification_dict = api_direct_certification_instance.to_dict()
# create an instance of APIDirectCertification from a dict
api_direct_certification_from_dict = APIDirectCertification.from_dict(api_direct_certification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


