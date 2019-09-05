import { Person } from './Common/Person'
import { Thing } from './Common/Thing'

export class Book extends Thing {
    genres?: string[];
    pageLength: number = 25;
    isbn?: string;
    author?: Person;
    price?: number;
}
