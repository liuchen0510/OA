package com.webtest.demo;
import static org.testng.Assert.assertTrue;

import java.io.IOException;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import com.webtest.core.BaseTest;
public class SearchTest extends BaseTest{
	Login_Action action;
	@BeforeMethod
	public void setup() throws IOException {
		action=new Login_Action(webtest);	
		Login_Action action =new Login_Action(webtest);
		action.login("admin", "123456");
	}
	@Test(priority=0)
	public void search1() {
		Search_Action search= new Search_Action(webtest);
		search.search1("01");
	}
	@Test(priority=0)
	public void search2() {
		Search_Action search= new Search_Action(webtest);
		search.search1("第一次投票");
	}
	@Test(priority=0)
	public void search3() {
		Search_Action search= new Search_Action(webtest);
		search.search1("");
	}
}
