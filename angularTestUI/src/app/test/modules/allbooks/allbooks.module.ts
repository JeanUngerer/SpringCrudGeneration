import { NgModule } from '@angular/core';
import {MatTableModule} from '@angular/material/table';
import { AllBooksListComponent } from './allbookslist/allbookslist.component';
import { AllBooksDetailComponent } from './allbooksdetail/allbooksdetail.component';
import { AllBooksCreateComponent } from './allbookscreate/allbookscreate.component';
import AllBooksRoutingModule from './allbooks-routing.module';
@NgModule({
	declarations: [
		AllBooksListComponent,
		AllBooksDetailComponent,
		AllBooksCreateComponent,
	],
	imports: [
MatTableModule,AllBooksRoutingModule,	]
	exports: [
	]
})
export class AllBooksModule { }
