import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AllBooksService } from './../../aServiceOutput/AllBooks.service';
import { AllBooks } from './../../aModelOutput/AllBooks.model';

@Component({
	selector: 'allbooks-list',
	templateUrl: 'allbooks.component.html',
	styleUrls: ['allbooks.component.scss']
})
export class AllBooksListComponent implements OnInit {
	allbooksList: AllBooks[];

	constructor(private allbooksService: AllBooksService, private router: Router) { }

	ngOnInit() {
		this.getAllBooksList();
	}

	getAllBooksList() {
		this.allbooksService.getAllAllBooks().subscribe(data => {
			this.allbooksList = data;
		});
	}

	onRowClick(id: number) {
		this.router.navigate(['allbooks', id]);
	}
}
