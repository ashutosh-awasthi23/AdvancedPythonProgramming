import requests
from requests.exceptions import RequestException


def del_req(u, i):
    delete_url = u + '/' + i

    try:
        response = requests.delete(delete_url)
        response.raise_for_status()
        if response.status_code == 204:
            print("User successfully deleted.")
        else:
            print("Failed to delete")
    except RequestException as e:
        print(f"{e}")


if __name__ == '__main__':
    url = 'https://reqres.in/api/users'
    u_id = '2'

    del_req(url, u_id)
