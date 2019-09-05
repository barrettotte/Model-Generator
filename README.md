# Model-Generator

Generate code for basic models from JSON schema for Java, Groovy, Kotlin, and TypeScript.


This is kind of a naïve implementation and isn't really too great in my opinion. I realized
its demise after messing with a non-jvm language. I'm struggling to find a way to strip out
common functionality with this current implementation.


In the future, it would be pretty sweet to try to marry Antlr grammars and JSON Schema to generate
classes more robustly with less generator code.


## Implemented Languages
- [x] Java 
- [x] Groovy
- [x] Kotlin -> 100% positive this isn't correct, I have no practical kotlin experience yet... will revisit
- [x] TypeScript


## Future Implementations ... When I feel like it
* T-SQL creation scripts
* Python
* Ruby
* C#
* ColdFusion (purely just masochism at this point)
* Scala
* Go


## Possible Improvements
* **DateTime** - I thought I had implemented this...might be going crazy
* **Parameterized constructor using 'required' on object properties**
* **On a similar note, call parameterized super constructor**
* Prefix my additional JSON schema props [extends, primitive, parseTo] with a '$'
* JPA Annotations
* Constants / final properties ?
* Serialization
* Builder methods ->  myModel.withProp1("wasd")
* hashCode, toString, and equals methods


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
* Test build Java Jar ```./tests-build/test-java.sh```
* Test build Groovy Jar ```./tests-build/test-groovy.sh```
* Test build Kotlin Jar ```./tests-build/test-kotlin.sh```


## References
* JSON Schema Core https://json-schema.org/latest/json-schema-core.html
* https://schema.org/docs/schemas.html
* https://json-schema.org/understanding-json-schema/index.html
* https://www.jsonschemavalidator.net/
* Inspiration https://app.quicktype.io/
* Kotlin default imports https://stackoverflow.com/questions/40075836/what-packages-functions-are-imported-by-default-in-kotlin
* Build a kotlin jar https://medium.com/@adrianmarkperea/understanding-gradle-by-creating-an-executable-kotlin-jar-8f554c7090c5