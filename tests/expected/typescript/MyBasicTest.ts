import { Address } from './Common/Address'
import { Thing } from './Common/Thing'

export class MyBasicTest extends Thing {
    myNumArray?: Array<number>;
    myNumArray2?: number[];
    myNumSet?: Array<number>;
    myStringList?: Array<string>;
    myInt?: number;
    myPrimInt?: number;
    myPrimBool?: boolean;
    myNestedList?: Array<Array<Address>>;
}
