# Model-Generator


Generate code for basic models from JSON schema. 


## Languages
- [x] Java 
- [x] Groovy
- [ ] Kotlin
- [ ] TypeScript
- [ ] T-SQL


## To Do
* unit tests for java and groovy before moving on
* generate build files in directories


## Possible Improvements
* Constants / final properties ?
* Serialization
* Builder methods
* hashCode, toString, and equals methods
* Parameterized constructor using 'required' on object properties
* On a similar note, call parameterized super constructor


## Specification
A couple of new properties were added to add more functionality.

* ```extends``` - extend from other object in another schema
* ```primitive``` - array: T[] or List<T> ; numbers: Float or float; Integer or int
* ```parseTo``` - attempt a parse to non-standard JSON schema types (BigDecimal, Long, Byte, etc)
  * If parsing fails on a field, it falls back to whatever is specified in ```type```


```JSON
{
  "id": "http://json-schema.org/thing",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Book",
  "description": "A book",
  "type": "object",
  "extends": {
    "$ref": "Common/Thing.json" // relative to schema directory
  },
  "properties": {
    "genres": {
      "type": "array",
      "items": {
        "type": "string", // String.class
        "maxItems": 10,   // String[10] init in constructor
        "primitive": true // true= T[], false/null= List<T>
      }
    },
    "pageLength": {
      "type": "integer",  // Integer.class
      "parseTo": "Long",  // attempt parse to Long.class
      "default": 25       // default value to 25 in constructor
    },
    "isbn": {
      "type": "string"
    },
    "author": {
      "$ref": "Common/Person.json" // Person.class relative to schema directory
    },
    "price": {
      "type": "number",    // Float.class
      "parseTo": "decimal" // attempt parse to BigDecimal for currency handling, falls back to Float if failed
    }
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
* Kotlin default imports https://stackoverflow.com/questions/40075836/what-packages-functions-are-imported-by-default-in-kotlin
* Build a kotlin jar https://medium.com/@adrianmarkperea/understanding-gradle-by-creating-an-executable-kotlin-jar-8f554c7090c5