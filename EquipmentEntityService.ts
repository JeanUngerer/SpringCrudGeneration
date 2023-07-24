import EquipmentEntityDTO from './EquipmentEntityDTO';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
	providedIn: 'root'
})
export class EquipmentEntityService {
	private baseUrl = '/api/equipment';

	constructor(private http: HttpClient) { }

	getAllEquipmentEntity(): Observable<EquipmentEntityDTO[]> {
		return this.http.get<EquipmentEntityDTO[]>(`${this.baseUrl}/equipments`);
	}

	getEquipmentEntity(id: number): Observable<EquipmentEntityDTO> {
		return this.http.get<EquipmentEntityDTO>(`${this.baseUrl}/${{id}}`);
	}

	createEquipmentEntity(equipmententity: EquipmentEntityDTO): Observable<EquipmentEntityDTO> {
		return this.http.put<EquipmentEntityDTO>(`${this.baseUrl}/create`, equipmententity);
	}

	updateEquipmentEntity(equipmententity: EquipmentEntityDTO): Observable<EquipmentEntityDTO> {
		return this.http.post<EquipmentEntityDTO>(`${this.baseUrl}/update`, equipmententity);
	}

	deleteEquipmentEntity(id: number): Observable<any> {
		return this.http.delete<any>(`${this.baseUrl}/${{id}}`);
	}
}
