package xxubin04.mvcpatternstudy;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MvcPatternStudyApplication {

	public static void main(String[] args) {

		Student model = retrieveStudentFromDatabase();

		StudentView view = new StudentView();

		StudentController controller = new StudentController(model, view);

		controller.updateView();  // StudentView 객체의 printStudentContent 호출

		controller.setStudentName("xxubin");  // 학생의 이름을 xxubin으로 설정

		controller.updateView();
	}

	private static Student retrieveStudentFromDatabase() {
		Student student = new Student();
		student.setName("Jeong");
		student.setRollNo("0123456");
		return student;
	}
}
