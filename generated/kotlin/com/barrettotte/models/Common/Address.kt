package com.barrettotte.models.common

import com.barrettotte.models.common.Thing

import com.fasterxml.jackson.module.kotlin.*

@JsonInclude(JsonInclude.Include.NON_NULL)
open class Address : Thing {
    var line1: String
    var line2: String
    var city: String
    var state: String
    var zip: String
}
