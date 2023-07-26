import {AllBooks} from './AllBooks.model';

export interface SpecialRule {
	id: number;
	name: string;
	phaseOfApplication: string;
	ruleText: string;
	book: AllBooks;
}
