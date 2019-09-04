package com.barrettotte.models

import com.barrettotte.models.common.Address
import com.barrettotte.models.common.Thing

import com.fasterxml.jackson.module.kotlin.*

@JsonInclude(JsonInclude.Include.NON_NULL)
open class MyBasicTest : Thing {
    var myNumArray: List<Float> = MutableList<Float>()
    var myNumArray2: Array<Float> = Array<Float>()
    var myNumSet: Set<Float> = MutableSet<Float>()
    var myStringList: List<String> = MutableList<String>()
    var myInt: Int
    var myPrimInt: Int
    var myPrimBool: Boolean
    var myNestedList: List<Set<Address>> = MutableList<MutableSet<Address>>()
}
