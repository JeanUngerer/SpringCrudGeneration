export interface Equipment {
	id: number;
	name: string;
	type: string;
	effects: string;
	book: AllBooks;
	specialRules: SpecialRule[];
}
