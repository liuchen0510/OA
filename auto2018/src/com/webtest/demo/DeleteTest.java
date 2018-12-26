package com.webtest.demo;
import static org.testng.Assert.assertTrue;

import java.io.IOException;

import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import com.webtest.core.BaseTest;
public class DeleteTest extends BaseTest {
	Login_Action action;
	@BeforeMethod
	public void setup() throws IOException {
		action=new Login_Action(webtest);
		Login_Action action =new Login_Action(webtest);
		action.login("admin", "123456");
	}
	@Test(priority=0)
	public void delete1() {
		Delete_Action delete= new Delete_Action(webtest);
		delete.delete1();
		assertTrue(webtest.ifContains("投票信息删除成功"));
	}
	@Test(priority=1)
	public void delete2() {
		Delete_Action delete= new Delete_Action(webtest);
		delete.delete2();
		assertTrue(webtest.ifContains("投票信息删除成功"));
	}
}
