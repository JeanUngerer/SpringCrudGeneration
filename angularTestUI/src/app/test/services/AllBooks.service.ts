import {AllBooks} from './../models/AllBooks.model';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
	providedIn: 'root'
})
export class AllBooksService {
	private baseUrl = '/api/equipment';

	constructor(private http: HttpClient) { }

	getAllAllBooks(): Observable<AllBooks[]> {
		return this.http.get<AllBooks[]>(`${this.baseUrl}/equipments`);
	}

	getAllBooks(id: number): Observable<AllBooks> {
		return this.http.get<AllBooks>(`${this.baseUrl}/${{id}}`);
	}

	createAllBooks(allbooks: AllBooks): Observable<AllBooks> {
		return this.http.put<AllBooks>(`${this.baseUrl}/create`, allbooks);
	}

	updateAllBooks(allbooks: AllBooks): Observable<AllBooks> {
		return this.http.post<AllBooks>(`${this.baseUrl}/update`, allbooks);
	}

	deleteAllBooks(id: number): Observable<any> {
		return this.http.delete<any>(`${this.baseUrl}/${{id}}`);
	}
}
