import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { EquipmentService } from './../../aServiceOutput/Equipment.service';
import { Equipment } from './../../aModelOutput/Equipment.model';

@Component({
	selector: 'equipment-list',
	templateUrl: 'equipment.component.html',
	styleUrls: ['equipment.component.scss']
})
export class EquipmentListComponent implements OnInit {
	equipmentList: Equipment[];

	constructor(private equipmentService: EquipmentService, private router: Router) { }

	ngOnInit() {
		this.getEquipmentList();
	}

	getEquipmentList() {
		this.equipmentService.getAllEquipment().subscribe(data => {
			this.equipmentList = data;
		});
	}

	onRowClick(id: number) {
		this.router.navigate(['equipment', id]);
	}
}
