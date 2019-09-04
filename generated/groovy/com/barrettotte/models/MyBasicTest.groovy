package com.barrettotte.models

import com.barrettotte.models.common.Address
import com.barrettotte.models.common.Thing

import com.fasterxml.jackson.annotation.JsonInclude
import com.fasterxml.jackson.annotation.JsonProperty

import java.util.List
import java.util.ArrayList
import java.util.Set
import java.util.HashSet

@JsonInclude(JsonInclude.Include.NON_NULL)
class MyBasicTest extends Thing {

    @JsonProperty("myNumArray")
    List<Float> myNumArray = new ArrayList<Float>()

    @JsonProperty("myNumArray2")
    Float[] myNumArray2 = new Float[10]

    @JsonProperty("myNumSet")
    Set<Float> myNumSet = new HashSet<Float>()

    @JsonProperty("myStringList")
    List<String> myStringList = new ArrayList<String>()

    @JsonProperty("myInt")
    Integer myInt

    @JsonProperty("myPrimInt")
    int myPrimInt

    @JsonProperty("myPrimBool")
    boolean myPrimBool

    @JsonProperty("myNestedList")
    List<Set<Address>> myNestedList = new ArrayList<HashSet<Address>>()

}
