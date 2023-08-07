import { NgModule } from '@angular/core';
import { EquipmentListComponent } from './equipmentlistcomponent/equipmentlistcomponent.component';
import { EquipmentDetailComponent } from './equipmentdetailcomponent/equipmentdetailcomponent.component';
import { EquipmentCreateComponent } from './equipmentcreatecomponent/equipmentcreatecomponent.component';

@NgModule({
	declarations: [
		EquipmentListComponent,
		EquipmentDetailComponent,
		EquipmentCreateComponent,
	],
	exports: [
		EquipmentListComponent,
		EquipmentDetailComponent,
		EquipmentCreateComponent,
	]
})
export class EquipmentModule { }
