package com.barrettotte.models

import com.barrettotte.models.common.Address
import com.barrettotte.models.common.Thing

import com.fasterxml.jackson.module.kotlin.*

@JsonInclude(JsonInclude.Include.NON_NULL)
open class Building : Thing {
    var address: Address = Address()
}
