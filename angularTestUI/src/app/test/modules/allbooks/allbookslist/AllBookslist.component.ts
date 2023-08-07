import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AllBooksService } from './../../../services/AllBooks.service';
import { AllBooks } from './../../../models/AllBooks.model';

@Component({
	selector: 'allbooks-list',
	templateUrl: 'allbookslist.component.html',
	styleUrls: ['allbookslist.component.scss']
})
export class AllBooksListComponent implements OnInit {
	allbooksList: AllBooks[] = [];

	constructor(private allbooksService: AllBooksService, private router: Router) { }

	ngOnInit() {
		this.getAllBooksList();
	}

	getAllBooksList() {
		this.allbooksService.getAllAllBooks().subscribe(data => {
			this.allbooksList = data as AllBooks[];
		});
	}

	onRowClick(id: number) {
		this.router.navigate(['allbooks', id]);
	}
}
