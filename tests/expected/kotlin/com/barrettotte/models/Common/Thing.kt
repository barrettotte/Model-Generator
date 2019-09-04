package com.barrettotte.models.common


import com.fasterxml.jackson.module.kotlin.*

@JsonInclude(JsonInclude.Include.NON_NULL)
open class Thing {
    var name: String
}
