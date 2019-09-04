package com.barrettotte.models.common

import com.barrettotte.models.common.Thing

import com.fasterxml.jackson.module.kotlin.*

@JsonInclude(JsonInclude.Include.NON_NULL)
open class Person : Thing {
    var age: Int
}
