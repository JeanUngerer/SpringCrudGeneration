import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {AllBooksListComponent} from "./allbookslist/AllBookslist.component";

const routes: Routes = [
	{ path: 'list', component: AllBooksListComponent },
];

@NgModule({
	imports: [RouterModule.forChild(routes)],
	exports: [RouterModule]
})
export class AllBooksRoutingModule { }
