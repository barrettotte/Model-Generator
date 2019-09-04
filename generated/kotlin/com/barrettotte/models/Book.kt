package com.barrettotte.models

import com.barrettotte.models.common.Person
import com.barrettotte.models.common.Thing

import com.fasterxml.jackson.module.kotlin.*

@JsonInclude(JsonInclude.Include.NON_NULL)
open class Book : Thing {
    var genres: Array<String> = Array<String>()
    var pageLength: Long = 25L
    var isbn: String
    var author: Person = Person()
    var price: BigDecimal = BigDecimal(0)
}
