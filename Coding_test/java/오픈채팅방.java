import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
public class 오픈채팅방 {
    
private static final String ENTER = "Enter";
private static final String LEAVE = "Leave";
private static final String CHANGE = "Change";

private static final String MESSAGE_ENTER = "님이 들어왔습니다.";
private static final String MESSAGE_LEAVE = "님이 나갔습니다.";

public static String[] solution(String[] record) {
    List<String[]> list = new ArrayList<>();
    Map<String, String> nickName = new HashMap<>();

    int returnArraySize = 0;
    for (String s : record) {
        String[] split = s.split(" ");
        String[] actionAndUid = new String[3];

        actionAndUid[0] = split[0];
        actionAndUid[1] = split[1];

        if (!CHANGE.equals(split[0])) {
            list.add(actionAndUid);
            returnArraySize++;
        }

        if (!LEAVE.equals(split[0])) {
            nickName.put(split[1], split[2]);
        }
    }

    String[] answer = new String[returnArraySize];
    int i = 0;
    for (String[] array : list) {
        switch (array[0]) {
            case ENTER :
                answer[i] = nickName.get(array[1]) + MESSAGE_ENTER;
                break;
            case LEAVE :
                answer[i] = nickName.get(array[1]) + MESSAGE_LEAVE;
                break;
        }

        i++;
    }

    return answer;
}
	public static void main(String[] args) {
        String[] record = {"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan","Enter uid1234 gandhi","Change uid4567 fuckyourmother","Enter uid1534 nepal","Enter uid8888 torpedo","Change uid4567 lexler","Change uid1534 shaker","Enter uid1534 changed"};
		System.out.println(solution(record));
	}

}