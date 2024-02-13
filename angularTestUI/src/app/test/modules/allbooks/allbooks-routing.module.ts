import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AllBooksModule } from './allbooks.module';

import { AllBooksListComponent } from './allbookslist/AllBookslist.component';
import { AllBooksDetailComponent } from './allbooksdetail/AllBooksdetail.component';
import { AllBooksCreateComponent } from './allbookscreate/AllBookscreate.component';
const routes: Routes = [
	{ path: 'list', component: AllBooksListComponent },
	{ path: 'detail/:id', component: AllBooksDetailComponent },
	{ path: 'create', component: AllBooksCreateComponent },
];

@NgModule({
	imports: [RouterModule.forChild(routes), AllBooksModule],
	exports: [RouterModule]
})
export class AllBooksRoutingModule { }
