import {Equipment} from './../aModelOutput/Equipment.model';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
	providedIn: 'root'
})
export class EquipmentService {
	private baseUrl = '/api/equipment';

	constructor(private http: HttpClient) { }

	getAllEquipment(): Observable<Equipment[]> {
		return this.http.get<Equipment[]>(`${this.baseUrl}/equipments`);
	}

	getEquipment(id: number): Observable<Equipment> {
		return this.http.get<Equipment>(`${this.baseUrl}/${{id}}`);
	}

	createEquipment(equipment: Equipment): Observable<Equipment> {
		return this.http.put<Equipment>(`${this.baseUrl}/create`, equipment);
	}

	updateEquipment(equipment: Equipment): Observable<Equipment> {
		return this.http.post<Equipment>(`${this.baseUrl}/update`, equipment);
	}

	deleteEquipment(id: number): Observable<any> {
		return this.http.delete<any>(`${this.baseUrl}/${{id}}`);
	}
}
