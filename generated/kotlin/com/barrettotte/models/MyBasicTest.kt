package com.barrettotte.models

open class Thing {
    var myNumArray: List<float>myNumArray = ArrayList<float>()
    var myNumArray2: float[] = float[10]
    var myNumSet: Set<Float>myNumSet = HashSet<Float>()
    var myStringList: List<String>myStringList = ArrayList<String>()
    var myInt: Integer
    var myPrimInt: int
    var myPrimBool: boolean
    var myNestedList: List<Set<Address>>myNestedList = ArrayList<HashSet<Address>>()
}

class MyBasicTest {

}
