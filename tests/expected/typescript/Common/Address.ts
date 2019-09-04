import { Thing } from '../Common/Thing'

export class Address extends Thing {
    line1?: string;
    line2?: string;
    city?: string;
    state?: string;
    zip?: string;
}
