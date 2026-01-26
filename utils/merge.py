import os
import glob

def merge_m3u(input_files, output_file,search_group_title="山东频道"):
    first_file = input_files[0]
    if not os.path.exists(first_file):
        print(f"文件 '{first_file}' 不存在，跳过。")
        return

    with open(first_file, "r") as input:
        lines = input.readlines()

    insert_position = -1
    for i in range(len(lines) - 1, -1, -1):
        if f'group-title="{search_group_title}"' in lines[i]:
            insert_position = i + 2
            break

    if insert_position == -1:
        print(f"在文件 '{first_file}' 中没有找到 group-title='{search_group_title}'。")
        insert_position = len(lines)

    second_file = input_files[1]
    if not os.path.exists(second_file):
        print(f"文件 '{second_file}' 不存在，跳过。")
        return

    with open(second_file, "r") as input:
        second_file_lines = input.readlines()

    with open(output_file, "w") as output:
        output.writelines(lines[:insert_position])
        output.writelines(second_file_lines)
        output.write("\n")
        output.writelines(lines[insert_position:])

    print(f"合并完成，输出到 {output_file}")


m3u_files = glob.glob("multicast/local/*.m3u")

city_dict = {}
for filepath in m3u_files:
    city = os.path.splitext(os.path.basename(filepath))[0]
    if city not in city_dict:
        city_dict[city] = []
    city_dict[city].append(filepath)

multicast_dir = "multicast"
output_dir = "multicast"
for city, append_files in city_dict.items():
    multicast_file = os.path.join(multicast_dir, f"multicast-{city}.m3u")
    output_file = os.path.join(output_dir, f"multicast-{city}.m3u")
    all_files = [multicast_file] + append_files
    merge_m3u(all_files,output_file)


