# New Repository AirBnB Clone (solo)
# contributor: Kevin Espinoza Salguedo

## Creating the first BaseModel Class

This part of the project focus on the creation of the main class named BaseModel, this class will contain all common
attributes and modules for other classes.

At this point you can create instances of the base class, the instance will inherit all the attributes and methods
of the base class and also can get new attributes by manipulating the instance.

```py
from models.base_model import BaseModel
# creating te instance
my_model = BaseModel()
# Adding new values
my_model.number = 86
# watch for format
my_model.to_dict()
```
Output:

```bash
{'id': 'ba725e96-5756-4051-97ce-bf03b339c3ee', 'created_at': '2024-03-23T18:31:25.358680', 'updated_at': '2024-03-23T18:31:25.358680', 'number': 86, '__class__': 'BaseModel'}
```

# Class Diagram BaseModel Test.
 ```mermaid
 classDiagram
  class BaseModel{
    +PubAtt id = str
    +PubAtt created_at = obj
    +PubAtt updated_at = obj
    +method special __str__() str
    Save() obj
    +method to_dict() str
  }
style BaseModel stroke:#000,stroke-width:6px


%%{
  init: {
    'theme': 'base',
    'themeVariables': {
      'primaryColor': '#005eff',
      'primaryTextColor': '#fff',
      'primaryBorderColor': '#000',
      'lineColor': '#000000',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff',
      'fontFamily': ''
    }
  }
}%%

<<Abstract>> BaseModel
 ```
> **_NOTE:_** As you can see in the class diagram the following public attributes "created_at" & "updated_at" are datetime objects (internally), we need to take care of this objects when printing the instance format, so inside the method  to_dict() we need to implement the logic to target those objects and convert those to strings.