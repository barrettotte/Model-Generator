package com.barrettotte.models.very.deep.directory

import com.barrettotte.models.common.Thing

import com.fasterxml.jackson.module.kotlin.*

@JsonInclude(JsonInclude.Include.NON_NULL)
open class Cat : Thing {
    var breed: String
    var color: String = "orange"
}
