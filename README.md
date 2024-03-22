# New Repository AirBnB Clone (solo)
# contributor: Kevin Espinoza Salguedo

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