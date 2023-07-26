import {AllBooks} from './AllBooks.model';
import {SpecialRule} from './SpecialRule.model';

export interface Equipment {
	id: number;
	name: string;
	type: string;
	effects: string;
	book: AllBooks;
	specialRules: SpecialRule[];
}
