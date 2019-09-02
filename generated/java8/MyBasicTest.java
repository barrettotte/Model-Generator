package com.barrettotte.models;

import com.barrettotte.models.common.Thing;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

import java.util.Set;
import java.util.List;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class MyBasicTest extends Thing {

    private float[] myNumArray;
    private Set<Float> myNumSet;
    private List<String> myStringList;
    private Integer myInt;
    private int myPrimInt;
    private boolean myPrimBool;
    private List<Set<Boolean>> myNestedList;


    @JsonProperty("myNumArray")
    public float[] getMyNumArray() {
        return this.myNumArray;
    }
    @JsonProperty("myNumArray")
    public void setMyNumArray(final float[] myNumArray) {
        this.myNumArray = myNumArray;
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
    public List<Set<Boolean>> getMyNestedList() {
        return this.myNestedList;
    }
    @JsonProperty("myNestedList")
    public void setMyNestedList(final List<Set<Boolean>> myNestedList) {
        this.myNestedList = myNestedList;
    }
}
