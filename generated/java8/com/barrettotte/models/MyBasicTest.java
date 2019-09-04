package com.barrettotte.models;

import com.barrettotte.models.common.Address;
import com.barrettotte.models.common.Thing;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class MyBasicTest extends Thing {

    private List<Float> myNumArray;
    private Float[] myNumArray2;
    private Set<Float> myNumSet;
    private List<String> myStringList;
    private Integer myInt;
    private int myPrimInt;
    private boolean myPrimBool;
    private List<Set<Address>> myNestedList;

    public MyBasicTest() {
        this.myNumArray = new ArrayList<Float>();
        this.myNumArray2 = new Float[10];
        this.myNumSet = new HashSet<Float>();
        this.myStringList = new ArrayList<String>();
        this.myNestedList = new ArrayList<HashSet<Address>>();
    }

    @JsonProperty("myNumArray")
    public List<Float> getMyNumArray() {
        return this.myNumArray;
    }
    @JsonProperty("myNumArray")
    public void setMyNumArray(final List<Float> myNumArray) {
        this.myNumArray = myNumArray;
    }

    @JsonProperty("myNumArray2")
    public Float[] getMyNumArray2() {
        return this.myNumArray2;
    }
    @JsonProperty("myNumArray2")
    public void setMyNumArray2(final Float[] myNumArray2) {
        this.myNumArray2 = myNumArray2;
    }

    @JsonProperty("myNumSet")
    public Set<Float> getMyNumSet() {
        return this.myNumSet;
    }
    @JsonProperty("myNumSet")
    public void setMyNumSet(final Set<Float> myNumSet) {
        this.myNumSet = myNumSet;
    }

    @JsonProperty("myStringList")
    public List<String> getMyStringList() {
        return this.myStringList;
    }
    @JsonProperty("myStringList")
    public void setMyStringList(final List<String> myStringList) {
        this.myStringList = myStringList;
    }

    @JsonProperty("myInt")
    public Integer getMyInt() {
        return this.myInt;
    }
    @JsonProperty("myInt")
    public void setMyInt(final Integer myInt) {
        this.myInt = myInt;
    }

    @JsonProperty("myPrimInt")
    public int getMyPrimInt() {
        return this.myPrimInt;
    }
    @JsonProperty("myPrimInt")
    public void setMyPrimInt(final int myPrimInt) {
        this.myPrimInt = myPrimInt;
    }

    @JsonProperty("myPrimBool")
    public boolean getMyPrimBool() {
        return this.myPrimBool;
    }
    @JsonProperty("myPrimBool")
    public void setMyPrimBool(final boolean myPrimBool) {
        this.myPrimBool = myPrimBool;
    }

    @JsonProperty("myNestedList")
    public List<Set<Address>> getMyNestedList() {
        return this.myNestedList;
    }
    @JsonProperty("myNestedList")
    public void setMyNestedList(final List<Set<Address>> myNestedList) {
        this.myNestedList = myNestedList;
    }
}
