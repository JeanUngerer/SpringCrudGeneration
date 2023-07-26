import {SpecialRule} from './../aModelOutput/SpecialRule.model';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
	providedIn: 'root'
})
export class SpecialRuleService {
	private baseUrl = '/api/equipment';

	constructor(private http: HttpClient) { }

	getAllSpecialRule(): Observable<SpecialRule[]> {
		return this.http.get<SpecialRule[]>(`${this.baseUrl}/equipments`);
	}

	getSpecialRule(id: number): Observable<SpecialRule> {
		return this.http.get<SpecialRule>(`${this.baseUrl}/${{id}}`);
	}

	createSpecialRule(specialrule: SpecialRule): Observable<SpecialRule> {
		return this.http.put<SpecialRule>(`${this.baseUrl}/create`, specialrule);
	}

	updateSpecialRule(specialrule: SpecialRule): Observable<SpecialRule> {
		return this.http.post<SpecialRule>(`${this.baseUrl}/update`, specialrule);
	}

	deleteSpecialRule(id: number): Observable<any> {
		return this.http.delete<any>(`${this.baseUrl}/${{id}}`);
	}
}
