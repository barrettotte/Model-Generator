# Model-Generator


Generate code for basic models from JSON schema. 


## Languages
- [ ] Java
- [ ] Groovy
- [ ] Kotlin
- [ ] TypeScript


## To Do
* Protected properties?
* folder structure for generated java classes


## Possible Enhancements
* Java: Constructor generation
* Java: toString, hashCode, equals


## Specification
```JSON
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Test schema",
    "description": "A test schema to show various things",
    "type": "object",
    "extends": {
        "$ref": "Common/Thing.json"
    },
    "properties": {
        "name": {
            "type": "string"
        },
        
    }
}
```


## Commands
* Run tests ```python -m unittest```


## References
* JSON Schema Core https://json-schema.org/latest/json-schema-core.html
* https://schema.org/docs/schemas.html
* https://json-schema.org/understanding-json-schema/index.html
* https://www.jsonschemavalidator.net/
* Inspiration https://app.quicktype.io/