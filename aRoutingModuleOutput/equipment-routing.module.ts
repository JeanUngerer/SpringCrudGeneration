import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { EquipmentModule } from './../aModuleOutput/equipment.module';

const routes: Routes = [
	{ path: 'list', component: EquipmentListComponent },
	{ path: 'detail/:id', component: EquipmentDetailComponent },
	{ path: 'create', component: EquipmentCreateComponent },
];

@NgModule({
	imports: [RouterModule.forChild(routes), EquipmentModule],
	exports: [RouterModule]
})
export class EquipmentRoutingModule { }
