import { NgModule } from '@angular/core';
import { AllBooksListComponent } from './allbookslistcomponent/allbookslistcomponent.component';
import { AllBooksDetailComponent } from './allbooksdetailcomponent/allbooksdetailcomponent.component';
import { AllBooksCreateComponent } from './allbookscreatecomponent/allbookscreatecomponent.component';

@NgModule({
	declarations: [
		AllBooksListComponent,
		AllBooksDetailComponent,
		AllBooksCreateComponent,
	],
	exports: [
		AllBooksListComponent,
		AllBooksDetailComponent,
		AllBooksCreateComponent,
	]
})
export class AllBooksModule { }
