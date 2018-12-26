package com.webtest.demo;
import static org.testng.Assert.assertTrue;

import java.io.IOException;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import com.webtest.core.BaseTest;
public class AddMeeting_Test extends BaseTest  {
	Login_Action action;
	@BeforeMethod
	public void setup() throws IOException {
		action=new Login_Action(webtest);
		Login_Action action =new Login_Action(webtest);
		action.login("admin", "123456");
	}
	@Test(priority=0)
	public void add1() {
		AddMeeting_Action add = new AddMeeting_Action(webtest);
		add.add("01");
		assertTrue(webtest.ifContains("会议室信息操作成功"));
	}
	@Test(priority=1)
	public void add2() {
		AddMeeting_Action add = new AddMeeting_Action(webtest);
		add.add("第一个");
		assertTrue(webtest.ifContains("会议室信息操作成功"));
	}
	@Test(priority=2)
	public void add3() {
		AddMeeting_Action add = new AddMeeting_Action(webtest);
		add.add("");
		assertTrue(webtest.ifContains("会议室名称不能为空"));
	}
}
