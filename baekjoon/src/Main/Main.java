package Main;

public class Main {
    public static String solution(String new_id) {
        String answer = "";
		//1단계 소문자 치환
		new_id = new_id.toLowerCase();
		String new_id2 ="";
		//2단계 소문자,숫자,-,_,.를 제외한 모든 문자를 제거.\
		char[] new_id_arr = new_id.toCharArray();
		for (char c : new_id_arr){
			if ((c>='a' && c <= 'z')||(c >= '0' && c <= '9')||c == '-' || c =='_'||c == '.'){
				new_id2 = new_id2+c;
			}
		}
		//3단계 마침표가 2개 이상 연속되면 1개로 바꿈.
		while(new_id2.contains("..")){
			new_id2 = new_id2.replace("..",".");
		}
		//4단계 앞 뒤의 마침표 제거
		if(new_id2.length() > 0){
			if(new_id2.charAt(0) == '.'){
				new_id2 = new_id2.substring(1,new_id2.length());
			}
		}
		if(new_id2.length() > 0){
			if(new_id2.charAt(new_id2.length()-1) == '.'){
				new_id2 = new_id2.substring(0,new_id2.length()-1);
			}
		}
		//5단계 id가 빈문자열이라면 new_id = "a"
		if(new_id2.length() == 0){
			new_id2 = "a";
		}
		//6단계 new_id의 길이가 16자 이상이면 15자까지 줄임.
		//만약 15번째 문자가 마침표라면 마침표 제거.
		if(new_id2.length()>15){
			new_id2 = new_id2.substring(0,15);
		}
		if(new_id2.charAt(new_id2.length()-1) == '.'){
			new_id2 = new_id2.substring(0,new_id2.length()-1);
		}
		while (new_id2.length()<=2){
			new_id2 += new_id2.substring(new_id2.length()-1,new_id2.length());
		}


		return new_id2;
    }
	public static void main(String[] args) {
		System.out.println(solution("ab"));
	}

}