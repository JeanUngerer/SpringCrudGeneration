import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SpecialRuleService } from './../../aServiceOutput/SpecialRule.service';
import { SpecialRule } from './../../aModelOutput/SpecialRule.model';

@Component({
	selector: 'specialrule-list',
	templateUrl: 'specialrule.component.html',
	styleUrls: ['specialrule.component.scss']
})
export class SpecialRuleListComponent implements OnInit {
	specialruleList: SpecialRule[];

	constructor(private specialruleService: SpecialRuleService, private router: Router) { }

	ngOnInit() {
		this.getSpecialRuleList();
	}

	getSpecialRuleList() {
		this.specialruleService.getAllSpecialRule().subscribe(data => {
			this.specialruleList = data;
		});
	}

	onRowClick(id: number) {
		this.router.navigate(['specialrule', id]);
	}
}
